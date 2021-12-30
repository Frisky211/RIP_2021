class Ajax {
    async get(url) {
        const response = await fetch(url, {
            method: "GET"
        });
        console.log()
        const responseData = await response.json();

        return {
            status: response.status,
            data: responseData
        };
    }
}

export const ajax = new Ajax();