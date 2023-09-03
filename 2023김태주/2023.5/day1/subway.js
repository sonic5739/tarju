const burgers = [
    {kor:"더블 빅맥",img:"https://www.mcdonalds.co.kr/upload/product/pcList/1683098039703.png",eng:"Double Big Mac"},
    {kor:"빅맥BLT",img:"https://www.mcdonalds.co.kr/upload/product/pcList/1683098321425.png",eng:"Big Mac BLT"},
    {kor:"빅맥",img:"https://www.mcdonalds.co.kr/upload/product/pcList/1583727841393.png",eng:"Big Mac"},
    {kor:"더블 쿼터파운즈치즈",img:"https://www.mcdonalds.co.kr/upload/product/pcList/1583727487454.png",eng:"Double quater pounder with cheese"},
    {kor:"쿼터파운드치즈",img:"https://www.mcdonalds.co.kr/upload/product/pcList/1583728183515.png",eng:"quater pounder with cheese"},
]


const box = document.getElementById('box')
    for (let i = 0; i<5;i++){

    box.insertAdjacentHTML("beforeend", `
    <div class="card">
    <div class="image"><img src="${burgers[i].img}" alt=""></div>
    <div class="write">
        <div class="korean">${burgers[i].kor}</div>
        <div class="english">${burgers[i].eng}</div>
    </div>
</div>`)
}