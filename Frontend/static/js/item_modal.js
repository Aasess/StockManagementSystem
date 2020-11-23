btn_datatable = document.querySelectorAll(".paginate_button");

function modal_display(){
    var items_detail = document.querySelectorAll("#stock_sale_add");
var item_name = document.querySelector("#modal_itemname");
var item_vendor = document.querySelector("#modal_itemvendor");
var item_qty = document.querySelector("#modal_itemqty");
var item_id = document.querySelector("#modal_itemid");

var item_name_sale = document.querySelector("#modal_itemname_sale");
var item_vendor_sale = document.querySelector("#modal_itemvendor_sale");
var item_qty_sale = document.querySelector("#modal_itemqty_sale");
var item_id_sale = document.querySelector("#modal_itemid_sale");
var item_sold_qty = document.querySelector("#modal_soldqty");

items_detail.forEach((item_detail)=>{
    item_detail.addEventListener("click",(e)=>{
        item_id.value = item_detail.text;
        item_name.value = item_detail.parentElement.parentElement.children[1].innerText
        item_vendor.value = item_detail.parentElement.parentElement.children[3].innerText
        item_qty.value = item_detail.parentElement.parentElement.children[4].innerText

        item_id_sale.value = item_detail.text;
        item_name_sale.value = item_detail.parentElement.parentElement.children[1].innerText
        item_vendor_sale.value = item_detail.parentElement.parentElement.children[3].innerText
        item_qty_sale.value = item_detail.parentElement.parentElement.children[4].innerText
        item_sold_qty.max = item_qty_sale.value;
})
})

}

modal_display();


btn_datatable.forEach((test)=>{
    test.addEventListener("click",()=>{
        modal_display();
    })
});
