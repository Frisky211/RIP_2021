class Urls {
    constructor() {
        this.url = 'http://localhost:8000/';
    }

    phones() {
        return `${this.url}phones/`
    }

    phone(id) {
        return `${this.url}phones/${id}/`
    }
}

export const urls = new Urls()