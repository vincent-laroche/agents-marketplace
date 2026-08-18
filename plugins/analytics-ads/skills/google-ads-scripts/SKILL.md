---
name: google-ads-scripts
description: "Automate Google Ads management with Google Ads Scripts — automated bidding rules, budget pacing, performance alerts, bulk keyword updates, campaign reporting, and label management. Use when automating Google Ads tasks."
---

# Google Ads Scripts

Automate Google Ads management using JavaScript-based Scripts — run directly in the Google Ads interface with no setup required.

## Access

Google Ads → Tools & Settings → Bulk Actions → Scripts

Scripts run in your browser context and have full access to your Google Ads account.

## Script Structure

```javascript
function main() {
  // Your script logic here
  
  Logger.log("Script started: " + new Date().toISOString());
  
  // Always log results for debugging
  Logger.log("Script completed successfully");
}
```

## Budget Pacing Script

Pause campaigns that have spent their monthly budget:

```javascript
function main() {
  var MONTHLY_BUDGET = 2000; // $2,000/month
  var today = new Date();
  var daysInMonth = new Date(today.getFullYear(), today.getMonth() + 1, 0).getDate();
  var dayOfMonth = today.getDate();
  var expectedSpend = (MONTHLY_BUDGET / daysInMonth) * dayOfMonth;
  
  var campaigns = AdsApp.campaigns()
    .withCondition("Status = ENABLED")
    .get();
  
  var totalSpend = 0;
  while (campaigns.hasNext()) {
    var campaign = campaigns.next();
    totalSpend += campaign.getStatsFor("THIS_MONTH").getCost();
  }
  
  Logger.log("Total spend this month: $" + totalSpend.toFixed(2));
  Logger.log("Expected spend at this point: $" + expectedSpend.toFixed(2));
  
  if (totalSpend > MONTHLY_BUDGET) {
    Logger.log("OVER BUDGET — pausing campaigns");
    // Add pause logic here
    sendAlert("Google Ads over monthly budget!", totalSpend);
  }
}

function sendAlert(subject, spend) {
  MailApp.sendEmail("info@hairsolutions.co", subject, 
    "Total spend: $" + spend.toFixed(2) + "\nCheck your Google Ads account.");
}
```

## Performance Alert Script

Get emailed when campaigns underperform:

```javascript
function main() {
  var ALERT_EMAIL = "info@hairsolutions.co";
  var CPA_THRESHOLD = 30; // Alert if CPA > $30
  var CTR_THRESHOLD = 0.02; // Alert if CTR < 2%
  
  var campaigns = AdsApp.campaigns()
    .withCondition("Status = ENABLED")
    .withCondition("Impressions > 100")
    .forDateRange("LAST_7_DAYS")
    .get();
  
  var alerts = [];
  
  while (campaigns.hasNext()) {
    var campaign = campaigns.next();
    var stats = campaign.getStatsFor("LAST_7_DAYS");
    
    var ctr = stats.getCtr();
    var conversions = stats.getConversions();
    var cost = stats.getCost();
    var cpa = conversions > 0 ? cost / conversions : null;
    
    if (ctr < CTR_THRESHOLD) {
      alerts.push(campaign.getName() + ": Low CTR = " + (ctr * 100).toFixed(1) + "%");
    }
    
    if (cpa !== null && cpa > CPA_THRESHOLD) {
      alerts.push(campaign.getName() + ": High CPA = $" + cpa.toFixed(2));
    }
  }
  
  if (alerts.length > 0) {
    MailApp.sendEmail(ALERT_EMAIL, 
      "Google Ads Performance Alert — " + new Date().toDateString(),
      "Performance issues detected:\n\n" + alerts.join("\n"));
    Logger.log("Alerts sent: " + alerts.length);
  }
}
```

## Keyword Bid Adjustment Script

Increase bids on high-converting keywords:

```javascript
function main() {
  var MIN_CONVERSIONS = 3;
  var TARGET_CPA = 20;
  var MAX_BID = 5.00;
  
  var keywords = AdsApp.keywords()
    .withCondition("Status = ENABLED")
    .withCondition("Conversions >= " + MIN_CONVERSIONS)
    .forDateRange("LAST_30_DAYS")
    .get();
  
  while (keywords.hasNext()) {
    var keyword = keywords.next();
    var stats = keyword.getStatsFor("LAST_30_DAYS");
    var conversions = stats.getConversions();
    var cost = stats.getCost();
    var cpa = cost / conversions;
    
    if (cpa < TARGET_CPA) {
      // Performing well — consider bid increase
      var currentBid = keyword.bidding().getCpc();
      var newBid = Math.min(currentBid * 1.1, MAX_BID); // 10% increase, cap at $5
      
      if (newBid > currentBid) {
        keyword.bidding().setCpc(newBid);
        Logger.log("Increased bid for: " + keyword.getText() + 
                   " from $" + currentBid + " to $" + newBid);
      }
    }
  }
}
```

## Weekly Performance Report

```javascript
function main() {
  var EMAIL = "info@hairsolutions.co";
  var report = [];
  
  report.push("Google Ads Weekly Report — " + new Date().toDateString());
  report.push("Period: Last 7 Days\n");
  report.push("CAMPAIGN PERFORMANCE:");
  report.push("Campaign | Clicks | Impressions | CTR | Conversions | Cost | CPA");
  report.push("-".repeat(80));
  
  var campaigns = AdsApp.campaigns()
    .withCondition("Status = ENABLED")
    .forDateRange("LAST_7_DAYS")
    .get();
  
  var totalCost = 0, totalConversions = 0, totalClicks = 0;
  
  while (campaigns.hasNext()) {
    var campaign = campaigns.next();
    var stats = campaign.getStatsFor("LAST_7_DAYS");
    
    var clicks = stats.getClicks();
    var impressions = stats.getImpressions();
    var ctr = impressions > 0 ? (clicks / impressions * 100).toFixed(1) + "%" : "0%";
    var conversions = stats.getConversions();
    var cost = stats.getCost();
    var cpa = conversions > 0 ? "$" + (cost / conversions).toFixed(2) : "N/A";
    
    totalCost += cost;
    totalConversions += conversions;
    totalClicks += clicks;
    
    report.push([
      campaign.getName().substring(0, 30),
      clicks, impressions, ctr, conversions.toFixed(0),
      "$" + cost.toFixed(2), cpa
    ].join(" | "));
  }
  
  report.push("\nTOTALS:");
  report.push("Total Spend: $" + totalCost.toFixed(2));
  report.push("Total Conversions: " + totalConversions.toFixed(0));
  report.push("Total Clicks: " + totalClicks);
  report.push("Overall CPA: $" + (totalConversions > 0 ? (totalCost / totalConversions).toFixed(2) : "N/A"));
  
  MailApp.sendEmail(EMAIL, "Google Ads Weekly Report", report.join("\n"));
  Logger.log("Report sent to " + EMAIL);
}
```

## Scheduling Scripts

In Google Ads → Scripts, set schedule:
- **Hourly**: Budget monitoring, impression share alerts
- **Daily**: Performance alerts, bid adjustments
- **Weekly**: Performance reports, budget pacing checks
- **Monthly**: Account health audit

## Best Practices

- Always preview changes with `campaign.pause()` replaced by `Logger.log("Would pause: " + campaign.getName())`
- Test on a small subset before running on all campaigns
- Add email alerts for exceptions (`MailApp.sendEmail()`)
- Use `AdsApp.currentAccount().getCustomerId()` to identify account in multi-account scripts
- Store configuration at top of script (thresholds, emails) for easy adjustment
- Version control your scripts (copy before editing)
