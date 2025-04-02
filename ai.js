async function sendMessage() {
    let userInput = document.getElementById("user-input").value;
    if (!userInput.trim()) return; // Ако е празно, не изпращай

    let chatBox = document.getElementById("chat-box");

    // Показва съобщението на потребителя с "You:"
    let userMessage = document.createElement("div");
    userMessage.className = "message user-message";
    userMessage.innerHTML = `<strong>You:</strong> ${userInput}`;
    chatBox.appendChild(userMessage);

    // Изпращане към Python сървъра
    try {
        let response = await fetch("http://127.0.0.1:5000/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message: userInput })
        });
        let data = await response.json();

        // Добавяме забавяне преди да изпратим отговор от чатбота
        setTimeout(() => {
            // Показва отговора от сървъра с "FootballMaster:"
            let botMessage = document.createElement("div");
            botMessage.className = "message bot-message";
            botMessage.innerHTML = `<strong>FootballMaster:</strong> ${data.response}`;
            chatBox.appendChild(botMessage);

            // Скролваме до последното съобщение
            chatBox.scrollTop = chatBox.scrollHeight;
        }, 1500); // Забавяне от 1.5 секунди
    } catch (error) {
        console.error("Грешка при свързване със сървъра:", error);
    }

    // Изчистване на полето за въвеждане
    document.getElementById("user-input").value = "";
}
