import React, {useEffect, useState} from "react";
import {useParams} from "react-router";
import {Table} from "react-bootstrap";
import Header from "../components/Header";
import Footer from "../components/Footer";
import GetPhoneByPK from "../modules/GetPhoneByPK";

function PhoneDetailPage() {
    const pk = useParams().pk;
    console.log(pk);

    const [phone, setPhone] = useState({});

    const handlePhone = async () => {
        const result = await GetPhoneByPK(pk);
        await setPhone(result);
    }

    useEffect(() => {
        handlePhone();}, []);

    useEffect(() => {
        console.log(phone);}, [phone])

    return (
        <div>
            <Header/>
            <Table striped bordered size="sm" className="fs-4">
                <tbody>
                <tr>
                    <td className="mx-2">Модель</td>
                    <td className="mx-2">{phone.model}</td>
                </tr>
                <tr>
                    <td className="mx-2">Описание</td>
                    <td className="mx-2">{phone.description}</td>
                </tr>
                <tr>
                    <td className="mx-2">Диаметр</td>
                    <td className="mx-2">{phone.diag}</td>
                </tr>
                <tr>
                    <td className="mx-2">Емкость аккумулятора</td>
                    <td className="mx-2">{phone.capacity}</td>
                </tr>
                </tbody>
            </Table>
            <Footer/>
        </div>
    );
}

export default PhoneDetailPage;