$('#myTable').DataTable({
    order: [0, 'desc'],
});



const loader = document.querySelector('.loader');
const content = document.querySelector('.display-content');

function init() {
  setTimeout(() => {
    loader.style.opacity = 0;
    loader.style.display = 'none';

    content.style.display = 'block';
    setTimeout(() => (content.style.opacity = 1), 50);
  }, 800);
}

init();



dateall = document.querySelectorAll("#date")
dateall.forEach((date)=>{
    date.innerText = moment(new Date(date.innerText)).format("YYYY-MM-DD, hh:mm A")
})
