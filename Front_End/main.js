document.addEventListener("DOMContentLoaded", function () {
    var currentDate = new Date();
    var selectedDate = new Date();
    displayDate(currentDate);

    document.getElementById("prev-date").addEventListener("click", function () {
        currentDate.setDate(currentDate.getDate() - 1);
        displayDate(currentDate);
    });

    document.getElementById("next-date").addEventListener("click", function () {
        currentDate.setDate(currentDate.getDate() + 1);
        displayDate(currentDate);
    });

            // Get the calendar-dates element
            const calendarDates = document.querySelector(".calendar-dates");

            // Add click event listener to the calendar dates
            calendarDates.addEventListener("click", function (event) {
                // Check if a date element is clicked
                if (event.target.tagName === "LI") {
                    // Get the clicked date
                    const clickedDate = parseInt(event.target.innerText);
        
                    // Set the date to the clicked date
                    selectedDate = new Date(currentDate);

					currdate.innerText = `${months[month]} ${year}`;
					displayDate(new Date(year, month, clickedDate));
                    // currentDate.setDate(clickedDate);
                    selectedDate.setDate(new Date(year, month, clickedDate));

					document.querySelectorAll(".calendar-dates li").forEach((dateElement) => {
						dateElement.classList.remove("selected");
					});
			
					// Add the "selected" class to the clicked date element
					event.target.classList.add("selected");

                    // Update the displayed date
                    // displayDate(selectedDate);

                    hideCalendar();
                }
            });



});

function displayDate(date) {
	console.log(date)

	var options = { year: 'numeric', month: 'long', day: 'numeric' };
	var day = { weekday: 'long' };
	var formattedDate = date.toLocaleDateString('en-US', options);
	var formattedDay = date.toLocaleDateString('en-US', day);

	document.getElementById("today-date").innerText = formattedDate;
	document.getElementById("today-day").innerText = formattedDay;
}



function hideCalendar() {
	var calendarContainer = document.querySelector('.calendar-container');
	calendarContainer.style.display = 'none';
}

let date = new Date();
let year = date.getFullYear();
let month = date.getMonth();

const day = document.querySelector(".calendar-dates");

const currdate = document
	.querySelector(".calendar-current-date");

const prenexIcons = document
	.querySelectorAll(".calendar-navigation span");

// Array of month names
const months = [
	"January",
	"February",
	"March",
	"April",
	"May",
	"June",
	"July",
	"August",
	"September",
	"October",
	"November",
	"December"
];

// Function to generate the calendar
const manipulate = () => {

	// Get the first day of the month
	let dayone = new Date(year, month, 1).getDay();

	// Get the last date of the month
	let lastdate = new Date(year, month + 1, 0).getDate();

	// Get the day of the last date of the month
	let dayend = new Date(year, month, lastdate).getDay();

	// Get the last date of the previous month
	let monthlastdate = new Date(year, month, 0).getDate();

	// Variable to store the generated calendar HTML
	let lit = "";

	// Loop to add the last dates of the previous month
	for (let i = dayone; i > 0; i--) {
		lit +=
			`<li class="inactive">${monthlastdate - i + 1}</li>`;
	}

	// Loop to add the dates of the current month
	for (let i = 1; i <= lastdate; i++) {

		// Check if the current date is today
		let isToday = i === date.getDate()
			&& month === new Date().getMonth()
			&& year === new Date().getFullYear()
			? "active"
			: "";
		lit += `<li class="${isToday}">${i}</li>`;
	}

	// Loop to add the first dates of the next month
	for (let i = dayend; i < 6; i++) {
		lit += `<li class="inactive">${i - dayend + 1}</li>`
	}

	// Update the text of the current date element 
	// with the formatted current month and year
	const formattedMonthYear = `${months[month]} ${year}`;
	currdate.innerText = formattedMonthYear;


	// update the HTML of the dates element 
	// with the generated calendar
	day.innerHTML = lit;
}

manipulate();

// Attach a click event listener to each icon
prenexIcons.forEach(icon => {

	// When an icon is clicked
	icon.addEventListener("click", () => {

		// Check if the icon is "calendar-prev"
		// or "calendar-next"
		month = icon.id === "calendar-prev" ? month - 1 : month + 1;

		// Check if the month is out of range
		if (month < 0 || month > 11) {

			// Set the date to the first day of the 
			// month with the new year
			date = new Date(year, month, new Date().getDate());

			// Set the year to the new year
			year = date.getFullYear();

			// Set the month to the new month
			month = date.getMonth();
		}

		else {

			// Set the date to the current date
			date = new Date();
		}

		// Call the manipulate function to 
		// update the calendar display
		manipulate();
	});
});

