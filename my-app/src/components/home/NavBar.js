import React, {Component} from "react"
import "./NavBar.scss"
import {Link} from "react-router-dom";

class NavBar extends Component {
    /**
     * @description the navigation bar
     * @call in every page
     */
    constructor(props) {
        super(props);
        this.state = {popup: false}
        this.setPopup = this.setPopup.bind(this)
    }
    setPopup() {
        this.setState({popup: !this.state.popup})
    }
    render() {
        if (localStorage.getItem("email") === "") {
            window.location.href = "/"
        }
        return <div className="navbar">
            <div className="logoApp">
                <Link className="linkTo" to="/home">
                    Accueil
                </Link>
            </div>
            <div className="searchIcon">
                <Link className="linkTo" to="/search">
                    Rechercher
                </Link>
            </div>
            <div className="reccoIcon">
                <Link className="linkTo" to="/reccomandation">
                    Recommandations
                </Link>
            </div>
            <div className="position">
                <Link className="linkTo" to={"/position"}>
                    Boîtes à livres
                </Link>
            </div>
            <div className="pastIcon">
                <Link className="linkTo" to="/historic">
                    Bibliothèque
                </Link>
            </div>
            <div className="userIcon">
                <Link className="linkTo" to="/user">
                    Mon compte
                </Link>
            </div>
            <div className="linkTo" onClick={() => {
                localStorage.setItem("email", "");
                window.location.href = "/"}
            }>
                Se déconnecter
            </div>
        </div>
    }
}

export default NavBar