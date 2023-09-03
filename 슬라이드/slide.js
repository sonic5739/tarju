function change(player, img){
    const select = document.querySelector("#select");
    select.innerHTML = player
    
    const selectIMG = document.querySelector("#selectImg")
    selectIMG.src = img
}