function init() {
    console.log("initialize");
}

function push_button() {
    (async () => {
        let result = await eel.add(1, 2)();
        console.log("result", result);
        document.getElementById("span_result").textContent = result;
    })();
}
