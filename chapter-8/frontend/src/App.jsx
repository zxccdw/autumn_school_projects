import React, { useEffect, useState } from 'react'
import './App.css'
import wikipedia from './assets/wikipedia.png';
import search from './assets/search.png';
import { observer } from 'mobx-react-lite';
import axios from 'axios';
import Store from './store/store';

export const App = observer(() => {
  const [input, setInput] = useState('');

  async function getSearch(word) {
    const req = await axios
      .get("localhost:8000/api/search/" + word)
      .then(response => {
        const temp = response.data;
        const keys = Object.keys(temp);
        const values = Object.values(temp);
        Store.makeEmpty();
        for(let i = 0; i < keys.length; i++){
          Store.setValue({title: keys[i], url: values[i]})
        }
      })
      .catch(error => {
        Store.makeEmpty();
        Store.setValue({title:"К сожалению произошла ошибка ответа от сервера", url: ''});
        console.error("Ошибка: ", error);
      })
  }

  const handleKeyDown = ((event) => {
    switch(event.key){
      case 'Enter':
        getSearch(input);
        break;
      default:
        break;
    }
  });

  return (
    <>
      <header>
        <nav style={{display: 'flex', width: '100%', alignItems: 'center', fontSize: '40px', fontWeight: '700', height: '100px', boxShadow: "0 0 4px 2px rgba(0,0,0,0.5)"}}>
          <img src={wikipedia}/>
          Wikipedia Searcher
        </nav>
      </header>
      <main style={{width: '1440px', display: 'flex', flexDirection: 'column', margin: 'auto', justifyContent: 'center', alignItems: 'center', marginTop: '100px'}}>
        <div style={{display: 'flex', width: "50%", marginBottom: '50px', justifyContent: 'center'}}>
          <div style={{display: 'flex', width: '60%', justifyContent: 'center'}}>
            <input onKeyDown={handleKeyDown} placeholder='Введите ваш запрос' onChange={(e) => setInput(e.target.value)} style={{width: '90%', height: '40px', border: '1px solid black', borderRadius: '10px', fontSize: '16px', paddingLeft: '10px'}}/>
          </div>
          <div style={{display: 'flex', justifyContent: 'center'}}>
            <button onClick={() => getSearch(input)} style={{cursor: 'pointer', border: '1px solid black', backgroundColor: 'white', borderRadius: '5px', alignContent: 'center'}}>
              <img src={search} style={{width: '40px', height: '40px', objectFit: 'cover'}}/>
            </button>
          </div>
        </div>
        <div style={{width: '40%'}}>
          {
            Store.request.map((element, index) => {
              if(element.url == false){
                return <a key={index}  style={{display: 'flex', width: 'calc(100%-10px)', marginTop: '20px', marginBottom: '20px', textAlign: 'center',  borderRadius: '8px', cursor: 'pointer', height: 'auto', minHeight:'40px', alignItems: 'center', fontSize: '35px', paddingLeft: '10px', textDecoration: 'none', color: 'red'}}>
                {element.title}
              </a> 
              }
            
              return(
                <a key={index} href={element.url} style={{display: 'flex', width: 'calc(100%-10px)', marginTop: '20px', marginBottom: '20px', borderRadius: '8px', cursor: 'pointer', height: 'auto', minHeight:'40px', boxShadow: '0 0 4px 2px rgba(0,0,0,0.5)', alignItems: 'center', fontSize: '35px', paddingLeft: '10px', textDecoration: 'none', color: 'black'}}>
                  {element.title}
                </a>)
            })
          }
        </div>
      </main>
    </>
  )
}
)

