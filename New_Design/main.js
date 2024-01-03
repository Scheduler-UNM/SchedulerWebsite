document.addEventListener("DOMContentLoaded", function () {
    var currentDate = new Date();
    displayDate(currentDate);

    document.getElementById("prev-date").addEventListener("click", function () {
        currentDate.setDate(currentDate.getDate() - 1);
        displayDate(currentDate);
    });

    document.getElementById("next-date").addEventListener("click", function () {
        currentDate.setDate(currentDate.getDate() + 1);
        displayDate(currentDate);
    });

    function displayDate(date) {
        var options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
        var formattedDate = date.toLocaleDateString('en-US', options);

        document.getElementById("today-date").innerText = formattedDate;
    }
});
