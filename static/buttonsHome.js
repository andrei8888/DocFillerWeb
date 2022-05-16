

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

scanButton.addEventListener("click",showPhoto);
function showPhoto() {
    sourcePath="static/uploads/".concat(fileInput.value.split(/(\\|\/)/g).pop())
    document.getElementById("photoShow").src=sourcePath;
    document.getElementById("progressBar").style.visibility = 'inherit';
    document.getElementById("photoShow").style.visibility = 'inherit';
    document.getElementById("infoHome").style.visibility = 'hidden';
}

/*var form = document.getElementById("formImage");
function handleForm(event) { event.preventDefault(); }
form.addEventListener('submit', handleForm);

function doScan(event) {
      event.preventDefault();
      document.getElementById("formImage").submit();
}

*/
