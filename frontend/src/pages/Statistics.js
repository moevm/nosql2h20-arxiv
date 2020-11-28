import React, {useState, useEffect, createRef} from "react";
import '../App.css';
import {Doughnut, Bar} from 'react-chartjs-2';
import Spinner from 'react-bootstrap/Spinner'
import Table from 'react-bootstrap/Table'

export default function Statistics() {
    const [data, setData] = useState([])
    const [bar_data, setBarData] = useState([])
    const [error, setError] = useState(false);
    const [isLoaded, setIsLoaded] = useState(false);
    const [result, setResult] = useState('');
    const [json, setJson] = useState([]);
    useEffect(() => {
        fetch(`http://localhost:5000/statistics`)
            .then(res => res.json())
            .then(
                (result) => {
                    setIsLoaded(true);
                    console.log(result, " - result")
                    setData(result[0]);
                    setBarData(result[1]);
                },
                (error) => {
                    setIsLoaded(true);
                    setError(error);
                }
            )
    }, [])
    if (error) {
        return <div>Ошибка: {error.message}</div>;
    } else if (!isLoaded) {
        return <Spinner animation="grow" />;
    } else {
        return (

            <div>
                <h2>10 people with higest article number</h2>
                <Doughnut data={data}/>
                <div>
                    <Bar
                        data={bar_data}
                        width={600}
                        height={400}
                    />
                </div>
            </div>
        );
    }
}