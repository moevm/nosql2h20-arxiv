import React, {useState, useEffect, createRef} from "react";
import {InputGroup, FormControl, Table, Button} from "react-bootstrap";
import BootstrapTable from "react-bootstrap-table-next";
import '../App.css';
import {Link} from 'react-router-dom'

export default function Co_author(props) {
    const [co_author, setAuthor] = useState('');
    const [error, setError] = useState(false);
    const [isLoaded, setIsLoaded] = useState(false);
    const [result, setResult] = useState('');
    const [json, setJson] = useState([]);

    useEffect(() => {
        fetch(`http://localhost:5000/co_author?co_author=${props.match.params.co_author}`)
            .then(res => res.json())
            .then(
                (result) => {
                    setIsLoaded(true);
                    console.log(result, " - result")
                    setJson(result);
                },
                (error) => {
                    setIsLoaded(true);
                    setError(error);
                }
            )
    }, [co_author])
    const columns = [
        {
            dataField: "name",
            text: 'Author name'
        },
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
                <div>
                    <h1>{props.match.params.co_author}</h1>
                </div>
                <Table>
                    <thead>
                        <tr>
                            {columns.map((value, index) => (
                                <th key={index}>{value.text}</th>
                            ))}
                        </tr>
                    </thead>
                    {json.map((json_value) => (
                        <tbody>
                            {json_value.co_authors.map((author) => (
                                <tr>
                                    <th>
                                        {author.name}
                                    </th>
                                    <th>
                                        {author.article_name}
                                    </th>

                                </tr>
                            ))}
                        </tbody>
                    ))}
                </Table>
                <Link to="/author">
                    <Button size="sm">
                        Back to author search
                    </Button>
                </Link>
                <Link to="/article">
                    <Button size="sm">
                        Back to article search
                    </Button>
                </Link>
            </div>
        );
    }
}
