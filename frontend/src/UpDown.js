import React from "react";
import { AiOutlineUpload, AiOutlineDownload } from "react-icons/ai";


export default function UpDown(props)

// props tells if the button will upload or download, based on whcih the text and symbol of the button will change. everything else remains the same

{
    const {isUp, onClick} = props
    const text = isUp ? "Upload" : "Download"
    const Icon = isUp ? AiOutlineUpload : AiOutlineDownload

    const handleChange = (e) => {
        if (isUp && e.target.files.length > 0) {
          onClick(e.target.files[0]);
        }
      };
      
    return (
        <div className="up-down-div">
            {isUp ? 
            (
                <label className="up-down-button">
                    {text} <Icon style={{backgroundColor: "#C29CE4", marginLeft: "0.3rem"}}/>
                    <input type="file" accept="video/*" onChange={handleChange} style={{display : 'none'}}/>
                </label>
            ) : (
            <button className="up-down-button" onClick={onClick}>
                {text} <Icon style={{backgroundColor: "#C29CE4", marginLeft: "0.3rem"}}/>
            </button>
            )}   
        </div>
    )
}