import React, {useEffect, useState} from "react";
import {Link} from "react-router-dom";
import Header from "../components/Header";
import Footer from "../components/Footer";
import GetPhones from "../modules/GetPhones";

function PhoneListPage() {

    const [phones, setPhones] = useState([]);

    const handlePhonesList = async () => {
        const results = await GetPhones();
        await setPhones(results);
    }

    useEffect(() => {
        handlePhonesList();
    }, []);


    return (
        <div>
            <Header/>
            <ul className="fs-4">
                {phones.map((phone) => {
                    return (<li key={phone.idphone}><Link to={"/phones/" + phone.idphone.toString()}
                                                     className="text-decoration-none link-dark">
                        {phone.model}</Link></li>);

                })}
            </ul>
            <Footer/>
        </div>
    );
}

export default PhoneListPage;
