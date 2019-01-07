// On a click on the browser action, send the app a message.
browser.browserAction.onClicked.addListener(() => {
    // Create new connect to the app so we can dl multiple stuff at same time.
    let port = browser.runtime.connectNative("web_video_dl");
    browser.tabs.query({currentWindow: true, active: true}).then((tab) => {
        tab = tab[0];
        console.log("Downloding: " + tab.url);
        port.postMessage(tab.url);
    });
});
