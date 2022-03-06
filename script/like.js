function likeNew()
{
    var list = document.getElementsByClassName("item qz_like_btn_v3 ");
    for (i = 0; i < list.length; i++)
    {
        if (list[i].attributes[6].value == 'like')
        {
            list[i].firstChild.click();
        }
    }
    document.getElementsByClassName("ui-icon  icon-refresh-v9")[0].click();
    return true;
}


function random(min, max)
{
    return Math.floor(Math.random() * (max - min)) + min;
}

function randomClock()
{
    const time = random(30000, 90000)
    const timer = setTimeout(() =>
    {
        likeNew();
        randomClock()
        clearTimeout(timer)
    }, time)

}

randomClock()