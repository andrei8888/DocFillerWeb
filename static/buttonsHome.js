

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
    deleteInformations()
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


deleteInfoButton=document.getElementById("deleteInfoButton");
deleteInfoButton.addEventListener("click",deleteInformations);
function deleteInformations(e) {
    var elems = document.getElementsByClassName("infos");
    for(var i=0;i<elems.length;i+=1) {
        elems[i].value = ''
    }
    saveInformations(e);
}


saveButton=document.getElementById("saveButton");
saveButton.addEventListener("click", saveInformations);
function saveInformations(e) {
    var url=window.location.pathname;
    var infoData = new FormData();
    var infoData = {
        nume: $("#nume").val(),
        prenume: $("#prenume").val(),
        cetatenie: $("#cetatenie").val(),
        domiciliu: $("#domiciliu").val(),
        emis: $("#emis").val(),
        seria: $("#seria").val(),
        nr: $("#nr").val(),
        cnp: $("#cnp").val(),
        sex: $("#sex").val(),
        dataNastere: $("#dataNastere").val(),
    };
    //console.log(infoData);
    $.ajax({
        method : "POST",
        url: "/home/info",
        data: JSON.stringify(infoData),
        contentType: "application/json; charset=utf-8",
        processData: false,
    });
    e.preventDefault();
}


$("#scaneazaPoza").click(function(e) {
    var form_data = new FormData();
    var files = $('#uploadPhoto')[0].files;
    if(files.length > 0 ){
        form_data.append("image_file",files[0]);
    }
    $.ajax({
      method : "POST",
      url: "/home/photoUpload",
      data: form_data,
      contentType: false,
      processData: false,
    })
    e.preventDefault();
    showPhoto();
});

function sleep(milliseconds) {
    const date = Date.now();
    let currentDate = null;
    do {
        currentDate = Date.now();
    } while (currentDate - date < milliseconds);
}
