let foods = JSON.parse(localStorage.getItem("foods")) || [];

let total = 0;
let expiring = 0;
let expired = 0;

// 🔥 Render function (IMPORTANT)
function renderTable() {
    let table = document.getElementById("foodTable");
    table.innerHTML = "";

    total = 0;
    expiring = 0;
    expired = 0;

    foods.forEach((item, index) => {

        let row = `
        <tr>
            <td>${item.food}</td>
            <td>${item.expiry}</td>
            <td class="${item.status.replace(/\s/g,'')}">${item.status}</td>
            <td>
                <button onclick="deleteFood(${index})">Delete</button>
            </td>
        </tr>
        `;

        table.innerHTML += row;

        total++;

        if (item.status === "Expiring Soon") expiring++;
        if (item.status === "Expired") expired++;
    });

    document.getElementById("totalItems").innerText = total;
    document.getElementById("expiringSoon").innerText = expiring;
    document.getElementById("expiredItems").innerText = expired;
}

// ✅ Add Food
function addFood() {

    let food = document.getElementById("foodName").value;
    let expiry = document.getElementById("expiryDate").value;

    if (food === "" || expiry === "") {
        alert("Please fill all fields");
        return;
    }

    let today = new Date();
    let expDate = new Date(expiry);

    let diff = Math.ceil((expDate - today) / (1000 * 60 * 60 * 24));

    let status = "";

    if (diff < 0) {
        status = "Expired";
    } else if (diff <= 3) {
        status = "Expiring Soon";
    } else {
        status = "Fresh";
    }

    foods.push({ food, expiry, status });

    localStorage.setItem("foods", JSON.stringify(foods));

    document.getElementById("foodName").value = "";
    document.getElementById("expiryDate").value = "";

    renderTable();
}

// ❌ Delete single item
function deleteFood(index) {

    foods.splice(index, 1);

    localStorage.setItem("foods", JSON.stringify(foods));

    renderTable();
}

// 🔄 Load on page start
window.onload = function () {
    renderTable();
};