function docButtons(len) {
    const documentNumber=len;

    for(let i=0;i<documentNumber;i++) {
        document.getElementById("docLabel"+i.toString()).addEventListener("click", function() {
            document.getElementById("thumbnailModal"+i.toString()).style.display = "block";
        });
    }


    closeButtons = document.getElementsByClassName("closeModalBtn");
    for (const closeButton of closeButtons)
        closeButton.addEventListener("click",closeModal);

    /*document.addEventListener("click",closeOnClickOutside(event));
    function closeOnClickOutside(event){
            if(!event.currentTarget.closest(".modal"))
                closeModal();
        }*/

    function closeModal() {
        modals=document.getElementsByClassName("modal");
        for (const modal of modals)
            modal.style.display = "none";
    }
}

document.getElementById("selectAllButton").addEventListener("click", selectAll)
function selectAll() {
    selectDocs = document.getElementsByClassName("form-check-input");
    for (const selectDoc of selectDocs)
        selectDoc.checked = true;
}

document.getElementById("unselectAllButton").addEventListener("click", unselectAll)
function unselectAll() {
    selectDocs = document.getElementsByClassName("form-check-input");
    for (const selectDoc of selectDocs)
        selectDoc.checked = false;
}
