from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rock', methods=['GET', 'POST'])
def rock():
    if request.method == 'POST':
        duration = request.form.get('duration')
        
        if duration == 'less':
            style_type = request.form.get('style_type')
            if style_type == 'natural':
                maintenance = request.form.get('maintenance')
                if maintenance == 'yes':
                    recommendation = "Try a slick back bun, high bun, or plaits."
                elif maintenance == 'no':
                    recommendation = "Try a twist/braid out, wash and go, or a natural half-up half-down."
            elif style_type == 'non-natural':
                maintenance = request.form.get('maintenance')
                if maintenance == 'yes':
                    recommendation = "Try a glueless wig, stitch braids, or a slick back bun with a braided ponytail."
                elif maintenance == 'no':
                    recommendation = "Try a quick weave (half-up half-down or all down), clip-ins, or a glued-down wig."
        
        elif duration == 'more':
            length = request.form.get('length')
            if length == 'long':
                recommendation = "Try bohemian braids, faux locs, sew-in, or Fulani braids."
            elif length == 'short':
                recommendation = "Try a sew-in bob, butterfly locs, a braided bob, or a pixie cut wig."
        
        else:
            recommendation = "Sorry, I didn't understand your choice."
        
        return render_template('rock.html', recommendation=recommendation)
    
    return render_template('rock.html')

if __name__ == "__main__":
    app.run(debug=True)
