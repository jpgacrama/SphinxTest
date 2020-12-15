function toggleNavBar() {
    var disp = document.getElementById('toggle-close').innerHTML
    if (disp === '&lt;&lt;') {
        console.log('To left!');
        document.getElementById('toggle-close').innerHTML = '&gt;&gt;';
        document.querySelector('.wy-nav-content-wrap').style.marginLeft = "35px";
        document.querySelector('.wy-nav-side').style.width = "35px";
        document.querySelector('.wy-nav-side').style.visibility = "hidden";
        document.getElementById('toggle-close').style.visibility = "visible";
    } else {
        console.log('To right!');
        document.getElementById('toggle-close').innerHTML = '&lt;&lt;';
        document.querySelector('.wy-nav-content-wrap').style.marginLeft = "300px";
        document.querySelector('.wy-nav-side').style.width = "300px";
        document.querySelector('.wy-nav-side').style.visibility = "visible";
        document.querySelector('.wy-nav-side').style.borderRight = "0px";
    }
}
