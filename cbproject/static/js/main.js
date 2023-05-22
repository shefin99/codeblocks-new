const scrollTop = document.getElementById('scrolltop')

window.onload = ()=>{
    scrollTop.style.visibility = "hidden";
    scrollTop.style.opacity = 0;
}

window.onscroll = ()=>{
    if(window.scrollY > 200){
        scrollTop.style.visibility = "visible";
        scrollTop.style.opacity = 1;
    }else{
        scrollTop.style.visibility = "hidden";
        scrollTop.style.opacity = 0;
    }
};
