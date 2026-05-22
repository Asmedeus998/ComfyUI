# Frontend JS Extensions

To update node UI after execution (e.g. display text), create a JS extension:

```javascript
// custom_nodes/<pack>/js/my_extension.js
import { app } from "../../scripts/app.js";
import { ComfyWidgets } from "../../scripts/widgets.js";

app.registerExtension({
    name: "my_pack.my_extension",
    async beforeRegisterNodeDef(nodeType, nodeData, app) {
        if (nodeData.name === "MyDisplayNode") {
            const onNodeCreated = nodeType.prototype.onNodeCreated;
            nodeType.prototype.onNodeCreated = function () {
                onNodeCreated?.apply(this, arguments);
                this.showValueWidget = ComfyWidgets["STRING"](
                    this, "value", ["STRING", { multiline: true }], app
                ).widget;
                this.showValueWidget.inputEl.readOnly = true;
            };

            const onExecuted = nodeType.prototype.onExecuted;
            nodeType.prototype.onExecuted = function (message) {
                onExecuted?.apply(this, arguments);
                if (message.text && this.showValueWidget) {
                    this.showValueWidget.value = message.text[0];
                }
            };
        }
    }
});
```

Python backend must return:
```python
return {"ui": {"text": (value,)}, "result": (value,)}
```

## Registering JS

Add to `custom_nodes/<pack>/__init__.py`:
```python
WEB_DIRECTORY = "./js"
```

Verify loaded: `curl http://127.0.0.1:8195/extensions | grep <pack>`
