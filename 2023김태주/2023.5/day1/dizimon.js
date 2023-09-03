function dizimonFetch(){                            
    return fetch("https://digimon-api.vercel.app/api/digimon")
    .then(response => response.json())
}
const all = []
const rookie = []
const in_training = []
const fresh = []
const ultimate = []
const armor = []
const mega = []
const champion = []

const box = document.getElementById('box')

function buttonclick(x){
    if(x=='all') randerdizimon(all)
    if(x=='Rookie') randerdizimon(rookie)
    if(x=='In-Training') randerdizimon(in_training)
    if(x=='Mega') randerdizimon(mega)
    if(x=='Armor') randerdizimon(armor)
    if(x=='Ultimate') randerdizimon(ultimate)
    if(x=='Champion') randerdizimon(champion)
    if(x=='Fresh') randerdizimon(fresh)
}
function randerdizimon(x){
    deletedizimon()
    makebox(x)
}   
function deletedizimon(){
    while(box.firstChild){
        box.firstChild.remove()
    }
}
function makebox(x){        
    x.forEach(data => {
        box.insertAdjacentHTML("beforeend", `
            <div class="card" style="width : 18rem">
                <img src="${data.img}" class = "card-img-top">
                <div class="card-body">
                    <h5 class="card-title">${data.name}</h5>
                    <p class="card-text">${data.level}</p>
                </div>
            </div>`)
})
}
dizimonFetch().then(data => {
    data.forEach(x =>{
        all.push(x)
        if(x.level == "In-Training") in_training.push(x)
        if(x.level == "Rookie") rookie.push(x)
        if(x.level == "Ultimate") ultimate.push(x)
        if(x.level == "Champion") champion.push(x)
        if(x.level == "Fresh") fresh.push(x)
        if(x.level == "Mega") mega.push(x)
        if(x.level == "Armor") armor.push(x)
    })
})
