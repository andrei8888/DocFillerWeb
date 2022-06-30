

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
    removeValidClasses();
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

saveSuccessInfo=document.getElementById("saveSuccess");
saveErrorInfo=document.getElementById("saveError");
saveEmptyInfo=document.getElementById("saveEmpty");
saveButton=document.getElementById("saveButton");
saveButton.addEventListener("click", saveInformations);
function saveInformations(e) {
    if(checkInfos() || emptyInfos()) {
        var url=window.location.pathname;
        var infoData = new FormData();
        var infoData = {
            nume: $("#nume").val(),
            prenume: $("#prenume").val(),
            cetatenie: $("#cetatenie").val(),
            locNastere: $("#locNastere").val(),
            domiciliu: $("#domiciliu").val(),
            emis: $("#emis").val(),
            seria: $("#seria").val(),
            nr: $("#nr").val(),
            cnp: $("#cnp").val(),
            sex: $("#sex").val(),
            dataNastere: $("#dataNastere").val(),
            dataEliberare: $("#dataEliberare").val(),
        };
        $.ajax({
            method : "POST",
            url: "/home/info",
            data: JSON.stringify(infoData),
            contentType: "application/json; charset=utf-8",
            processData: false,
        });
        e.preventDefault();
        if(!emptyInfos()) {
            saveSuccessInfo.style.display="block";
            saveErrorInfo.style.display="none";
            saveEmptyInfo.style.display="none";
            allInfosGood();
        }
        else {
            saveSuccessInfo.style.display="none";
            saveErrorInfo.style.display="none";
            saveEmptyInfo.style.display="block";
            removeValidClasses();
            window.scrollTo(0, 0);
        }
    }
    else {
        saveSuccessInfo.style.display="none";
        saveErrorInfo.style.display="block";
        saveEmptyInfo.style.display="none";
        showWhichError();
        window.scrollTo(0, 0);
    }
}

document.getElementById("scaneazaPoza").addEventListener("click",resetProgressBar);
function resetProgressBar() {
    var progressBar = document.getElementById("scanProgressBar");
    progressBar.style.width = "0%";
    progressBar.style.display = "none";
    progressBar.style.display = "block";
}

$("#scaneazaPoza").click(showAndScan);
function showAndScan(e){
    deleteInformations(event);
    sleep(1000);
    var progressBar = document.getElementById("scanProgressBar");
    progressBar.style.width = "0".concat("%");
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
    updateProgressBar();
    sleep(1500);
    var jqxhr = $.getJSON( 'static/uploads/saved_infos/infos.json', function(infos) {
        setInfos(infos);
    });
};

function updateProgressBar() {
  var progressBar = document.getElementById("scanProgressBar");
  var width = 1;
  var identity = setInterval(scene, 10);
  function scene() {
    if (width >= 100) {
      clearInterval(identity);
    } else {
      width++;
      progressBar.style.width = width + '%';
    }
  }
}

function setInfos(infos) {
    document.getElementById("nume").value = infos.nume;
    document.getElementById("prenume").value = infos.prenume;
    document.getElementById("cetatenie").value = infos.cetatenie;
    document.getElementById("locNastere").value = infos.locNastere;
    document.getElementById("domiciliu").value = infos.domiciliu;
    document.getElementById("emis").value = infos.emis;
    document.getElementById("seria").value = infos.seria;
    document.getElementById("nr").value = infos.nr;
    document.getElementById("cnp").value = infos.cnp;
    document.getElementById("sex").value = infos.sex;
    document.getElementById("dataNastere").value = infos.dataNastere;
    document.getElementById("dataEliberare").value = infos.dataEliberare;
}

function sleep(milliseconds) {
    const date = Date.now();
    let currentDate = null;
    do {
        currentDate = Date.now();
    } while (currentDate - date < milliseconds);
}

var RE_nume = new RegExp("^[-A-ZĂÎȘȚÂ]{3,}");
var RE_prenume = new RegExp("^[-A-ZĂÎȘȚÂ']{3,}$");
var RE_cetatenie = new RegExp("^[A-ZĂÎȘȚÂa-zăîșțâ]{3,} \/ [A-Z]{3}$");
var RE_locNastere = new RegExp("^Jud.[A-Z]{1,2} Mun.[-A-ZĂÎȘȚÂa-zăîșțâ]{3,}$");
var RE_domiciliu = new RegExp("^Jud.[A-Z]{1,2} Mun.[-A-ZĂÎȘȚÂa-zăîșțâ]{3,}\n[A-ZĂÎȘȚÂa-zăîșțâ0-9. ]{3,}$");
var RE_emis = new RegExp("^[-A-ZĂÎȘȚÂa-zăîșțâ. ]{3,}$");
var RE_seria = new RegExp("^[A-Z]{2}$");
var RE_nr = new RegExp("^\\d{6}$");
var RE_cnp = new RegExp("^[1-8]\\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\\d|3[01])(0[1-9]|[1-4]\\d|5[0-2]|99)(00[1-9]|0[1-9]\\d|[1-9]\\d\\d)\\d$");
var RE_sex = new RegExp("^(Masculin)|(Feminin)$");
var RE_dataNastere = new RegExp("^((([0-2]\\d)|(3[0-1]))\\.((0[1-9])|(1[0-2]))\\.((19\\d\\d)|(20[0-2]\\d)))$");
var RE_dataEliberare = new RegExp("^((([0-2]\\d)|(3[0-1]))\\.((0[1-9])|(1[0-2]))\\.((\\d\\d)))$");


function checkInfos() {
    var good;
    good = (RE_nume.test($("#nume").val())) &&
        (RE_prenume.test($("#prenume").val())) &&
        (RE_cetatenie.test($("#cetatenie").val())) &&
        (RE_locNastere.test($("#locNastere").val())) &&
        (RE_domiciliu.test($("#domiciliu").val())) &&
        (RE_emis.test($("#emis").val())) &&
        (RE_seria.test($("#seria").val())) &&
        (RE_nr.test($("#nr").val())) &&
        (RE_cnp.test($("#cnp").val())) &&
        (RE_sex.test($("#sex").val())) &&
        (RE_dataNastere.test($("#dataNastere").val())) &&
        (RE_dataEliberare.test($("#dataEliberare").val()));
    return good;
}

function emptyInfos() {
    return $("#nume").val() === "" &&
        $("#prenume").val() === "" &&
        $("#cetatenie").val() === "" &&
        $("#locNastere").val() === "" &&
        $("#domiciliu").val() === "" &&
        $("#seria").val() === "" &&
        $("#nr").val() === "" &&
        $("#cnp").val() === "" &&
        $("#sex").val() === "" &&
        $("#dataNastere").val() === "" &&
        $("#dataEliberare").val() ==="";
}

function showWhichError() {
    if(RE_nume.test($("#nume").val()))
        document.getElementById("nume").classList.add("is-valid");
    else
        document.getElementById("nume").classList.add("is-invalid");
    if(RE_prenume.test($("#prenume").val()))
        document.getElementById("prenume").classList.add("is-valid");
    else
        document.getElementById("prenume").classList.add("is-invalid");
    if(RE_cetatenie.test($("#cetatenie").val()))
        document.getElementById("cetatenie").classList.add("is-valid");
    else
        document.getElementById("cetatenie").classList.add("is-invalid");
    if(RE_locNastere.test($("#locNastere").val()))
        document.getElementById("locNastere").classList.add("is-valid");
    else
        document.getElementById("locNastere").classList.add("is-invalid");
    if(RE_domiciliu.test($("#domiciliu").val()))
        document.getElementById("domiciliu").classList.add("is-valid");
    else
        document.getElementById("domiciliu").classList.add("is-invalid");
    if(RE_emis.test($("#emis").val()))
        document.getElementById("emis").classList.add("is-valid");
    else
        document.getElementById("emis").classList.add("is-invalid");
    if(RE_seria.test($("#seria").val()))
        document.getElementById("seria").classList.add("is-valid");
    else
        document.getElementById("seria").classList.add("is-invalid");
    if(RE_nr.test($("#nr").val()))
        document.getElementById("nr").classList.add("is-valid");
    else
        document.getElementById("nr").classList.add("is-invalid");
    if(RE_cnp.test($("#cnp").val()))
        document.getElementById("cnp").classList.add("is-valid");
    else
        document.getElementById("cnp").classList.add("is-invalid");
    if(RE_sex.test($("#sex").val()))
        document.getElementById("sex").classList.add("is-valid");
    else
        document.getElementById("sex").classList.add("is-invalid");
    if(RE_dataNastere.test($("#dataNastere").val()))
        document.getElementById("dataNastere").classList.add("is-valid");
    else
        document.getElementById("dataNastere").classList.add("is-invalid");
    if(RE_dataEliberare.test($("#dataEliberare").val()))
        document.getElementById("dataEliberare").classList.add("is-valid");
    else
        document.getElementById("dataEliberare").classList.add("is-invalid");
}

function allInfosGood() {
    var elems = document.getElementsByClassName("infos");
    for(var i=0;i<elems.length;i+=1) {
        elems[i].classList.remove("is-invalid");
        elems[i].classList.add("is-valid");
    }
}

function removeValidClasses() {
    var elems = document.getElementsByClassName("infos");
    for(var i=0;i<elems.length;i+=1) {
        elems[i].classList.remove("is-invalid");
        elems[i].classList.remove("is-valid");
    }
}
