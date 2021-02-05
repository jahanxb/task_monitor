const BrowserHistory = require('node-browser-history');


//Only All Support Browser History

/**
 * Get Internet Explorer History
 * @param historyTimeLength time is in minutes
 * @returns {Promise<array>}
 */

getIEHistory(10).then(function (history) {
  console.log(history);
});

