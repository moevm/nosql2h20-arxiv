import React, {useState, useEffect, createRef} from "react";
import {InputGroup, FormControl, Table} from "react-bootstrap";
import '../App.css';

export default function Article() {
    const [article, setArticle] = useState('');
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
            setArticle(inf.value)
        }
    }

    useEffect(() => {
        //console.log('fetch',author)
        fetch(`http://localhost:5000/article?article=${article}`)
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
    }, [article])

    const columns = [
        {
            dataField: "article_name",
            text: 'Article name'
        },
        {
            dataField: "author_name",
            text: 'Author name'
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
                <input ref={inform}/>
                <button onClick={handleChange}>Search</button>
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
                                <th><a href={'http://localhost:3000/article_page/'+json_value.article_name}>{json_value.article_name}</a></th>
                                <th><a href={'http://localhost:3000/author_page/'+json_value.author_name}>{json_value.author_name}</a></th>
                            </tr>
                        ))}
                    </tbody>
                </Table>
            </div>
        );
    }
}
