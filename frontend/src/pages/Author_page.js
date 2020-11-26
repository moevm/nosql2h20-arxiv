import React, {useState, useEffect, createRef} from "react";
import {InputGroup, FormControl, Table,Button} from "react-bootstrap";
import BootstrapTable from "react-bootstrap-table-next";
import '../App.css';
import { Link } from 'react-router-dom'

export default function Author_page(props) {
    const [author_page, setAuthor] = useState('');
    const [error, setError] = useState(false);
    const [isLoaded, setIsLoaded] = useState(false);
    const [result, setResult] = useState('');
    const [json, setJson] = useState([]);

    useEffect(() => {
        console.log(props)
        fetch(`http://localhost:5000/author_page?author_page=${props.match.params.author_page}`)
            .then(res => res.json())
            .then(
                (result) => {
                    setIsLoaded(true);
                    console.log(result," - result")
                    setJson(result);
                },
                (error) => {
                    setIsLoaded(true);
                    setError(error);
                }
            )
    }, [author_page])

    const columns = [
        {
            dataField: "article",
            text: 'Article name'
        }
    ];
    if (error) {
        return <div>Ошибка: {error.message}</div>;
    } else if (!isLoaded) {
        return <div>Загрузка...</div>;
    } else {
        //console.log(author)
        //console.log(json)
        return (
            <div>
                <div><h1>{props.match.params.author_page}</h1></div>
                <Table>
                    <thead>
                        <tr>
                            {columns.map((value, index) => (
                                <th key={index}>{value.text}</th>
                            ))}
                        </tr>
                    </thead>
                    <tbody>
                        {json.map((json_value, index) => (
                            <tr key={index}>
                                <th><a href={'http://localhost:3000/article_page/'+json_value.article}>{json_value.article}</a></th>
                            </tr>
                        ))}
                    </tbody>
                </Table>
                <Link to="/author">
                    <Button size="lg">
                        Back to author search
                    </Button>
                </Link>
                <Link to="/article">
                    <Button size="lg">
                        Back to article search
                    </Button>
                </Link>
            </div>
        );
    }
}
