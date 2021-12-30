export class PhoneCardComponent {
    constructor(parent) {
        this.parent = parent;
    }

    getHTML(data) {
        return (
            `
                <div class="card" style="width: 300px;">
                    <img class="card-img-top" src="https://wallbox.ru/resize/1600x1200/wallpapers/main/201628/46cba6e5d7b3aac.jpg" alt="картинка">
                    <div class="card-body">
                        <h5 class="card-title">${data.model}</h5>
                        <p class="card-text">${data.description}</p>
                        <button class="btn btn-primary" id="click-card-${data.idphone}" data-id="${data.idphone}">Нажми на меня</button>
                    </div>
                </div>
            `
        )
    }

    addListeners(data, listener) {
        document
            .getElementById(`click-card-${data.idphone}`)
            .addEventListener("click", listener)
    }

    render(data, listener) {
        const html = this.getHTML(data)
        this.parent.insertAdjacentHTML('beforeend', html)
        this.addListeners(data, listener)
    }
}