console.log("script.js loaded");
async function sendQuestion(){

    let question =
        document.getElementById("question").value;

    let chatBox =
        document.getElementById("chat-box");

    chatBox.innerHTML +=
        `<div class="user"><b>You:</b> ${question}</div>`;

    const response = await fetch("/ask",{
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body:JSON.stringify({
            question:question
        })
    });

    const data = await response.json();

    chatBox.innerHTML +=
        `<div class="bot"><b>Assistant:</b> ${data.answer}</div>`;

    document.getElementById("question").value="";

    chatBox.scrollTop =
        chatBox.scrollHeight;
}