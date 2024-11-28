import React from 'react'
import './pred_page.css'
const pred = () => {
  return (
    <div>

    <div className="main_div">

        <div className='md_name'>preferfgreged</div>
    </div>
    <div className="pred">
        <div className='wid'>

        <div className='clas'>
            <div className="ct_block">

            <div className='namee'>cat</div>
            <div className='img ct_img'>cat</div>
            </div>

            <div className="dg_block">

            <div className='namee'>dog...../</div>
            <div className="bck_div"></div>
            <div className='img dg_img'>dog...../</div>
            </div>

        </div>
        <div class="button-container">
    <div class="button upload-button" data-hover-text="Upload Image to get prediction...">Upload</div>
    <div class="button predict-button" >Predict</div>
</div>

        </div>
    </div>


    </div>
  )
}

export default pred


