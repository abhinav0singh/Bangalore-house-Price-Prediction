window.onload = function() {
  fetch("http://127.0.0.1:5000/get_location_names")
    .then(response => response.json())
    .then(data => {
      const locationSelect = document.getElementById("location");
      locationSelect.innerHTML = "";

      data.locations.forEach(loc => {
        const option = document.createElement("option");
        option.text = loc;
        option.value = loc;
        locationSelect.appendChild(option);
      });
    })
    .catch(err => {
      alert("Failed to load location list. Check server.");
    });
};

function onClickedEstimatePrice() {
  const sqft = parseFloat(document.getElementById("sqft").value);
  const bhk = parseInt(document.getElementById("bhk").value);
  const bath = parseInt(document.getElementById("bath").value);
  const location = document.getElementById("location").value;
  const result = document.getElementById("result");

  if (!sqft || !bhk || !bath || !location) {
    result.innerText = "❌ Please fill all fields.";
    return;
  }

  result.innerText = "⏳ Predicting...";

  fetch("http://127.0.0.1:5000/predict_home_price", {
    method: "POST",
    mode: "cors",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      total_sqft: sqft,
      bhk: bhk,
      bath: bath,
      location: location
    })
  })
    .then(response => {
      if (!response.ok) {
        throw new Error("Network response was not ok.");
      }
      return response.json();
    })
    .then(data => {
      result.innerText = `✅ Estimated Price: ₹ ${data.estimated_price} Lakhs`;
    })
    .catch(error => {
      console.error("Prediction error:", error);
      result.innerText = "❌ Prediction failed. Check server log.";
    });
}
