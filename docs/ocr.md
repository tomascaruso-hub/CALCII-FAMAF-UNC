# Conversor de Imágenes a LaTeX (OCR)

Esta es una herramienta experimental integrada directamente en la página para facilitar la transcripción de fotos de apuntes, matrices y demostraciones a código LaTeX y lenguaje natural. El resultado te lo entregará formateado y listo para copiar y pegar en tu editor.

!!! warning "Límites de uso diario"
    Actualmente, el motor de inteligencia artificial funciona bajo un esquema gratuito. Esto significa que tenemos una **cantidad limitada de peticiones**. Si en época de parciales la herramienta se satura de fotos, es posible que el servidor devuelva un mensaje de error temporal.

!!! success "El futuro del proyecto"
    Si la herramienta resulta de utilidad, recibe el apoyo esperado y vemos que la adopción aumenta, la idea es mejorar la integración e invertir en una infraestructura sin límites de peticiones.

---
<div class="ocr-container" style="border: 1px solid var(--md-default-fg-color--lightest); padding: 1.5rem; border-radius: 8px; margin-top: 1.5rem; background-color: var(--md-default-bg-color);">
  
  <div id="dropZone" style="border: 2px dashed var(--md-primary-fg-color); border-radius: 8px; padding: 2rem; text-align: center; cursor: pointer; transition: background-color 0.2s ease; margin-bottom: 1rem;">
    <span style="font-size: 2.5rem; display: block; margin-bottom: 0.5rem;">📥</span>
    <p style="margin: 0; font-weight: bold; color: var(--md-default-fg-color);">Arrastrá tu captura de pantalla acá</p>
    <p style="margin: 0; font-size: 0.85em; color: var(--md-default-fg-color--light);">o hacé clic para buscar en tu compu</p>
    
    <input type="file" id="imageInput" accept="image/*" style="display: none;">
  </div>

  <div id="previewContainer" style="display: none; text-align: center; margin-bottom: 1rem;">
    <img id="imagePreview" src="" alt="Previsualización" style="max-width: 100%; max-height: 250px; border-radius: 6px; border: 1px solid var(--md-default-fg-color--lightest);">
    <p id="fileName" style="font-size: 0.85em; color: var(--md-default-fg-color--light); margin-top: 0.5rem;"></p>
  </div>
  
  <button id="convertBtn" class="md-button md-button--primary" style="width: 100%;" disabled>Procesar Imagen</button>
  
  <p id="loadingText" style="display: none; margin-top: 1rem; color: var(--md-primary-fg-color); text-align: center; font-weight: bold;">
    <span class="twemoji">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 2A10 10 0 1 0 22 12A10 10 0 0 0 12 2Zm0 18a8 8 0 1 1 8-8 8 8 0 0 1-8 8Z"/><path d="M12 6a1 1 0 0 0-1 1v5.25l4.5 2.67a.9.9 0 0 0 1.25-.32.9.9 0 0 0-.32-1.25L13 11.2V7a1 1 0 0 0-1-1Z"/></svg>
    </span>
    Analizando los cálculos en la nube...
  </p>
  
  <pre><code id="resultOutput" style="display: block; margin-top: 1rem; white-space: pre-wrap; min-height: 80px;">// El código aparecerá acá //</code></pre>

</div>

<script>
  document.addEventListener("DOMContentLoaded", function() {
    const dropZone = document.getElementById("dropZone");
    const fileInput = document.getElementById("imageInput");
    const previewContainer = document.getElementById("previewContainer");
    const imagePreview = document.getElementById("imagePreview");
    const fileNameDisplay = document.getElementById("fileName");
    const btn = document.getElementById("convertBtn");
    const resultBox = document.getElementById("resultOutput");
    const loading = document.getElementById("loadingText");

    let currentFile = null;

    document.addEventListener("paste", function(e) {
      // archivos en el portapapeles
      const items = e.clipboardData.items;
      for (let i = 0; i < items.length; i++) {
        if (items[i].type.indexOf("image") !== -1) {
          const file = items[i].getAsFile();
          e.preventDefault(); // evitamos que el navegador haga cosas raras
          const date = new Date();
          const autoName = `captura_portapapeles_${date.getHours()}${date.getMinutes()}${date.getSeconds()}.png`;
          const renamedFile = new File([file], autoName, { type: file.type });
          handleFile(renamedFile);
          break; 
        }
      }
    });

    // abrir selector al hacer clic en la zona
    dropZone.addEventListener("click", () => fileInput.click());

    // manejo de arrastrar y soltar
    dropZone.addEventListener("dragover", (e) => {
      e.preventDefault();
      dropZone.style.backgroundColor = "var(--md-primary-fg-color--transparent)";
    });

    dropZone.addEventListener("dragleave", () => {
      dropZone.style.backgroundColor = "transparent";
    });

    dropZone.addEventListener("drop", (e) => {
      e.preventDefault();
      dropZone.style.backgroundColor = "transparent";
      
      if (e.dataTransfer.files.length > 0) {
        handleFile(e.dataTransfer.files[0]);
      }
    });

    // manejo de selección clásica
    fileInput.addEventListener("change", function() {
      if (this.files.length > 0) {
        handleFile(this.files[0]);
      }
    });

    // previsualizar
    function handleFile(file) {
      if (!file.type.startsWith("image/")) {
        alert("Por favor, subí o pegá únicamente un archivo de imagen.");
        return;
      }

      currentFile = file;
      fileNameDisplay.textContent = file.name;
      btn.disabled = false; // Habilitamos el botón
      
      const reader = new FileReader();
      reader.onload = function(e) {
        imagePreview.src = e.target.result;
        previewContainer.style.display = "block";
        dropZone.style.display = "none"; // Ocultamos la caja gigante
      };
      reader.readAsDataURL(file);
    }

    // Botón de procesar
    if (!btn) return; 
    btn.addEventListener("click", async function() {
      if (!currentFile) return;

      // Desactivamos el botón y mostramos carga
      btn.disabled = true;
      btn.textContent = "Procesando...";
      loading.style.display = "block";
      resultBox.textContent = "";

      const formData = new FormData();
      formData.append("image", currentFile);

      try {
        const workerUrl = "https://latex-conversor-1.tomycaruso.workers.dev";
        
        const response = await fetch(workerUrl, {
          method: "POST",
          body: formData
        });

        const textResult = await response.text();
        
        if (!response.ok) throw new Error(textResult);

        resultBox.textContent = textResult;

      } catch (error) {
        resultBox.textContent = "Error de conexión: " + error.message;
      } finally {
        loading.style.display = "none";
        btn.textContent = "Procesar Imagen";
        btn.disabled = false;
      }
    });
  });
  // Error de conexión: NetworkError when attempting to fetch resource.
  //Error de conexión: Ocurrió un problema: This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.
</script>

