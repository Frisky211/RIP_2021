const GetPhones = async () => {
    return await fetch(`http://localhost:8000/phones/`, {method: "GET"})
        .then((response) => {
            return response.json();
        }).catch(() => {
            return {resultCount: 0, results: []};
        });
}

export default GetPhones;
