<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Code Tester</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css">
    <style>
        :root {
            --background-color: #000;
            --container-color: #000;
        }
        body {
            background-color: var(--background-color);
            font-family: Arial, sans-serif;
            color: #fff;
        }
        .container {
            max-width: 1200px;
            margin: 40px auto;
            background-color: var(--container-color);
            padding: 20px;
            border: 1px solid #555;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
        }
        .code-box {
            width: 100%;
            height: 200px;
            padding: 10px;
            border: 1px solid #555;
            border-radius: 5px;
            resize: vertical;
            background-color: #000;
            color: #fff;
        }
        iframe {
            width: 100%;
            height: 400px;
            border: 1px solid #555;
            border-radius: 5px;
        }
        .tab-content {
            padding: 20px;
        }
        .nav-link {
            color: #fff;
        }
        .nav-link:hover {
            color: #ccc;
        }
        #save-modal {
            display: none;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1 class="text-center">Code Tester</h1>
        <ul class="nav nav-tabs" id="myTab" role="tablist">
            <li class="nav-item" role="presentation">
                <button class="nav-link active" id="home-tab" data-bs-toggle="tab" data-bs-target="#home" type="button" role="tab" aria-controls="home" aria-selected="true">HTML</button>
            </li>
            <li class="nav-item" role="presentation">
                <button class="nav-link" id="profile-tab" data-bs-toggle="tab" data-bs-target="#profile" type="button" role="tab" aria-controls="profile" aria-selected="false">CSS</button>
            </li>
            <li class="nav-item" role="presentation">
                <button class="nav-link" id="contact-tab" data-bs-toggle="tab" data-bs-target="#contact" type="button" role="tab" aria-controls="contact" aria-selected="false">JavaScript</button>
            </li>
        </ul>
        <div class="tab-content" id="myTabContent">
            <div class="tab-pane fade show active" id="home" role="tabpanel" aria-labelledby="home-tab">
                <h2>HTML</h2>
                <textarea class="code-box" id="html-code"></textarea>
            </div>
            <div class="tab-pane fade" id="profile" role="tabpanel" aria-labelledby="profile-tab">
                <h2>CSS</h2>
                <textarea class="code-box" id="css-code"></textarea>
            </div>
            <div class="tab-pane fade" id="contact" role="tabpanel" aria-labelledby="contact-tab">
                <h2>JavaScript</h2>
                <textarea class="code-box" id="js-code"></textarea>
            </div>
        </div>
        <h2>Preview</h2>
        <iframe id="preview-frame" sandbox="allow-scripts" style="background-color: #fff;"></iframe>
        <button class="btn btn-primary" id="save-button" onclick="openSaveModal()">Save Code</button>
        <div id="save-modal" class="modal">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title">Save Code</h5>
                        <button type="button" class="btn-close" onclick="closeSaveModal()"></button>
                    </div>
                    <div class="modal-body">
                        <input type="text" id="filename" placeholder="Filename">
                        <button class="btn btn-primary" id="save-code-button" onclick="saveCode()">Save</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"></script>
    <script>
        const htmlCode = document.getElementById('html-code');
        const cssCode = document.getElementById('css-code');
        const jsCode = document.getElementById('js-code');
        const previewFrame = document.getElementById('preview-frame');
        const saveButton = document.getElementById('save-button');
        const saveModal = document.getElementById('save-modal');
        const filenameInput = document.getElementById('filename');
        const saveCodeButton = document.getElementById('save-code-button');

        function updatePreview() {
            const html = htmlCode.value;
            const css = cssCode.value;
            const js = jsCode.value;

            const doc = new DOMParser().parseFromString(html, 'text/html');
            const style = document.createElement('style');
            style.textContent = css;
            doc.head.appendChild(style);

            const script = document.createElement('script');
            script.textContent = js;
            doc.body.appendChild(script);

            previewFrame.srcdoc = `<style>body { background-color: #fff; color: #000; }</style>` + doc.documentElement.outerHTML;
        }

        htmlCode.addEventListener('input', updatePreview);
        cssCode.addEventListener('input', updatePreview);
        jsCode.addEventListener('input', updatePreview);

        function openSaveModal() {
            saveModal.style.display = 'block';
        }

        function closeSaveModal() {
            saveModal.style.display = 'none';
        }

        function saveCode() {
            const code = {
                html: htmlCode.value,
                css: cssCode.value,
                js: jsCode.value,
            };
            const json = JSON.stringify(code);
            const blob = new Blob([json], { type: 'application/json' });
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = filenameInput.value + '.json';
            a.click();
            closeSaveModal();
        }

        updatePreview();
    </script>
</body>
</html>