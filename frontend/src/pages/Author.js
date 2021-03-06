import React, {useState, useEffect, createRef} from "react";
import {InputGroup, FormControl, Table} from "react-bootstrap";
import '../App.css';
import Spinner from 'react-bootstrap/Spinner'

export default function Author() {
    const [author, setAuthor] = useState('');
    const [error, setError] = useState(false);
    const [isLoaded, setIsLoaded] = useState(false);
    const [result, setResult] = useState('');
    const [json, setJson] = useState([]);
    let inform = createRef();
    // Примечание: пустой массив зависимостей [] означает, что
    // этот useEffect будет запущен один раз
    // аналогично componentDidMount()

    const handleChange = () => {
        //console.log('AAAAA')
        const inf = inform.current;
        if (inf !== null) {
            //console.log(inf.value)
            setAuthor(inf.value)
        }
    }

    useEffect(() => {
        //console.log('fetch',author)
        fetch(`api/author?author=${author}`)
            .then(res => res.json())
            .then(
                (result) => {
                    setIsLoaded(true);
                    setJson(result);
                },
                // Примечание: важно обрабатывать ошибки именно здесь, а не в блоке catch(),
                // чтобы не перехватывать исключения из ошибок в самих компонентах.
                (error) => {
                    setIsLoaded(true);
                    setError(error);
                }
            )
    }, [author])

    const columns = [
        {
            dataField: "name",
            text: 'Author name'
        },
        {
            dataField: "article",
            text: 'Article name'
        },
        {
            dataField: "category",
            text: 'Category name'
        }
    ];
    if (error) {
        return <div>Ошибка: {error.message}</div>;
    } else if (!isLoaded) {
        return <Spinner animation="grow" />;
    } else {
        //console.log(author)
        //console.log(json)
        return (
            <div>
                <input ref={inform}/>
                <button onClick={handleChange}>Search</button>
                <Table variant="dark">
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
                                <th><a href={'http://localhost:3000/author_page/'+json_value.id}>{json_value.name}</a></th>
                                <th><a href={'http://localhost:3000/article_page/'+json_value.article_id}>{json_value.article}</a></th>
                                <th>{json_value.category}</th>
                            </tr>
                        ))}
                    </tbody>
                </Table>
            </div>
        );
    }
}
