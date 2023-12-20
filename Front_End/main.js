window.onload = () => {
    const tab_switchers = document.querySelectorAll('[data-switcher]');

    for (let i = 0; i< tab_switchers.length; i++)
    {
        const tab_switcher = tab_switchers[i];
        const page_id = tab_switcher.dataset.tab;

        tab_switcher.addEventListener('click',() =>{
            document.querySelector('.tabs .tab.is-Active').classList.remove('is-Active');
            tab_switcher.parentNode.classList.add('is-Active');

            switchPage(page_id);

        });
    }

}

function switchPage(page_id)
{
    console.log(page_id);
    const current_page = document.querySelector('.pages .page.is-Active');
    current_page.classList.remove('is-Active');

    const next_page = document.querySelector(`.pages .page[data-page = "${page_id}"]`);
    next_page.classList.add('is-Active');

}