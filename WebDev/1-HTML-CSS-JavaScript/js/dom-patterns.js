function showPattern(){
    const colorsArr = ['red', 'orange', 'yellow', 'greeen', 'blue', 'indigo', 'voilet'];

    let topPosition = 25;
    let leftPosition = 25; 
    let width = 500;
    let height = 500;
    let borderRadius = 100; 

    while(width > 50){
        const randomColorIdx = Math.floor(Math.random() * colorsArr.length); 
        const newDiv = document.createElement('div'); 

        newDiv.style.top = topPosition + 'px';
        newDiv.style.left = leftPosition + 'px';
        newDiv.style.width = width + 'px';
        newDiv.style.height = height + 'px';
        newDiv.style.borderRadius = borderRadius + 'px'; 
        newDiv.style.background  = colorsArr[randomColorIdx];

        document.body.appendChild(newDiv);
        topPosition += 10; 
        leftPosition +=10;
        width -= 20; 
        height -= 20;
        borderRadius += 2; 
    }

}