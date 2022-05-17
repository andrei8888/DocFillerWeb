

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
    document.getElementById("infoHome").style.visibility = 'visible';
    var elems = document.getElementsByClassName("hidden_elem");
    for(var i=0;i<elems.length;i+=1) {
        elems[i].style.display = 'none'
    }
    fileInput.value = "";
    handleButtons();

    document.getElementById("photoShow").src="#";
}

function showPhoto() {
    document.getElementById("infoHome").style.visibility = 'hidden';
    var elems = document.getElementsByClassName("hidden_elem");
    for(var i=0;i<elems.length;i+=1) {
        elems[i].style.display = 'block'
    }
    sleep(100);
    sourcePath="static/uploads/".concat(fileInput.value.split(/(\\|\/)/g).pop())
    document.getElementById("photoShow").src=sourcePath;
}


function sleep(milliseconds) {
  const date = Date.now();
  let currentDate = null;
  do {
    currentDate = Date.now();
  } while (currentDate - date < milliseconds);
}

/*var form = document.getElementById("formImage");
function handleForm(event) { event.preventDefault(); }
form.addEventListener('submit', handleForm);

function doScan(event) {
      event.preventDefault();
      document.getElementById("formImage").submit();
}

*/
