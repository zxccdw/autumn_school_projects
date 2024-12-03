import { makeAutoObservable } from "mobx";


class Store {
    request = [{title: '', url: ''}];

    constructor(){
        makeAutoObservable(this);
    }

    setValue(temp){
        this.request.push(temp);
    }

    makeEmpty(){
        this.request.length = 0;
    }
}

export default new Store();