import React from 'react';
import './Home.css';

const About = () => {
    const backgroundImageUrl = 'https://images.unsplash.com/photo-1613374933062-7aa9f54036ce?q=80&w=1888&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D';

    return (
        <div className="about-container" style={{backgroundImage: `url(${backgroundImageUrl})`}}>
            <div className="content-box">
                <h1 className="title"></h1>
                <p className="description">
                    Hi we are Shutter!
                </p>
            </div>
        </div>
    );
};

export default About;
