$('#myTable').DataTable({
    order: [0, 'desc'],
    "columnDefs": [
      { "orderable": false,
        "targets": [-1,-2]
      },
      { data: 'created_at', render: datetimepretty() },
      { data: 'price', render: moneypretty() }
    ]
});



const loader = document.querySelector('.loader');
const content = document.querySelector('.display-content');
btn_datatable = document.querySelectorAll(".paginate_button");



function init() {
  setTimeout(() => {
    loader.style.opacity = 0;
    loader.style.display = 'none';

    content.style.display = 'block';
    setTimeout(() => (content.style.opacity = 1), 50);
  }, 800);
}

function datetimepretty(){
  dateall = document.querySelectorAll("#date")
  dateall.forEach((date)=>{
  date.innerText = moment(new Date(date.innerText)).format("YYYY-MM-DD, hh:mm A")
})
}

init();

function moneypretty(){
  money = document.querySelectorAll(".money")
  money.forEach((mon)=>{
  mon.innerText = (parseInt(mon.textContent)).toFixed(1).replace(/\d(?=(\d{3})+\.)/g, '$&,');
})

}


$('#myModal').on('shown.bs.modal', function () {
  $('#myInput').trigger('focus')
})