const itemoutput = document.querySelector("tbody");

//funtions
function getItem(){
    fetch('http://127.0.0.1:8000/api/item/')
    .then((response)=> response.json())
    .then((data) => {
        itemoutput.innerText = "";
        data['data'].forEach((object)=>{
            itemoutput.innerHTML += `
            <tr>
            <td>${ object.sku }</td>
            <td>${ object.item_name }</td>
            <td>${ object.category }</td>
            <td>${ object.price }</td>
            <td>${ object.vendor }</td>
            <td>${ object.remaining_quantity }</td>
            <td>${ object.created_at }</td>
            <td>${ object.is_stock }</td>
            </tr>
        `;
        })
    })
}


getItem();

$(document).ready(function() {
    $('#test').DataTable();
} );

//events
