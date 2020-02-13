//Listen to form submit
document.getElementById('contactForm').addEventListener('submit',submitForm)

function submitForm(e){
    e.preventDefault();
 
    var number = document.getElementById('telNumber').value;
    console.log(number)
    saveNumber(number)
    
}


function saveNumber(number){
    console.log("here")

    db.collection('costumerInfo').add({
        contact: number,
        date : firebase.firestore.FieldValue.serverTimestamp()
    })

}