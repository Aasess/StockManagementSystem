const itemoutput = document.querySelector("tbody");

//funtions

function getToken(){
    return new Promise((resolve)=> {
        fetch('http://127.0.0.1:8000/api/gettoken/',{
        method: 'POST',
        headers: {
            'Accept':'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            'username': 'ashish',
            'password':'1234'
        })
    })
    .then((res) => res.json())
    .then((data)=> {
        resolve(data['access'])
    })
    })
}

function getItem(token){
    var bearer = 'Bearer ' + token;
    fetch('http://127.0.0.1:8000/api/item/',{
        method: 'GET',
        withCredentials: true,
        credentials: 'include',
        headers: {
            'Authorization': bearer,
            //'Content-Type': 'application/json'
        }

    })
    .then((response)=> response.json())
    .then((data) => {
        //itemoutput.innerText = "";
        data['data'].forEach((object)=>{
            itemoutput.innerHTML += `
            <tr>
            <td>${ object.sku }</td>
            <td>${ object.item_name }</td>
            <td>${ object.category_detail.category_name }</td>
            <td>${ object.price }</td>
            <td>${ object.vendor_detail.name }</td>
            <td class="pl-5">${ object.remaining_quantity }</td>
            <td>${ moment(new Date(object.created_at)).format("MMM.DD,YYYY, HH:mm A") }</td>
            <td id="is_stock">${ object.is_stock }</td>
            </tr>
        `;
        })
        const stock_value = document.querySelectorAll("#is_stock");
        stock_value.forEach((d)=>{
            if(d.innerText == "true"){
                d.innerHTML = `<img src ="http://127.0.0.1:8000/static/admin/img/icon-yes.svg">`;
            }
            else{
                d.innerHTML = `<img src ="http://127.0.0.1:8000/static/admin/img/icon-no.svg">`;
            }
        });
    })
    
}



getToken().then(getItem);

//events
