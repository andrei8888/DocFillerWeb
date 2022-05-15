

const fileInput = document.getElementById('uploadPhoto');
const scanButton = document.getElementById('scaneazaPoza');
const deleteImageButton = document.getElementById('stergePoza');

fileInput.addEventListener("change",handleButtons);

function handleButtons(){
    if(fileInput.files.length===0) {
        scanButton.disabled=true;
        deleteImageButton.disabled=true;
    }
    else {
        scanButton.disabled=false;
        deleteImageButton.disabled=false;
    }
};

deleteImageButton.addEventListener("click",deletePicture);
function deletePicture() {
    fileInput.value = "";
    handleButtons()
}

/*var form = document.getElementById("formImage");
function handleForm(event) { event.preventDefault(); }
form.addEventListener('submit', handleForm);

function doScan(event) {
      event.preventDefault();
      document.getElementById("formImage").submit();
}

*/
