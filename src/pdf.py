from fpdf import FPDF 

def pdf_creator(table):
    pdf = FPDF(format = 'A4', unit = 'cm')
    pdf.add_page('L')
    epw = pdf.w - 2*pdf.l_margin
    col_width = epw/10
    pdf.set_font('Times','B',18.0) 
    th = pdf.font_size
    #title 
    pdf.cell(epw, 0.0, 'Best restaurants', align='C')
    pdf.set_font('Times','',12.0) 
    pdf.ln(1)

    #creating the header
    pdf.cell(col_width, th+1, 'Name', align='C', border = 1)
    pdf.cell(col_width, th+1, 'City', align='C', border = 1)
    pdf.cell(col_width, th+1, 'Rating', align='C', border = 1)
    pdf.cell(col_width, th+1, 'Tag1', align='C', border = 1)
    pdf.cell(col_width, th+1, 'Tag2', align='C', border = 1)
    pdf.cell(col_width, th+1, 'Tag3', align='C', border = 1)
    pdf.cell(col_width, th+1,'Tag4', align='C', border = 1)
    pdf.cell(col_width, th+1, 'Tag5', align='C', border = 1)
    pdf.cell(col_width, th+1,'Phone_numbers', align='C', border = 1)
    pdf.cell(col_width, th+1, 'Range_Price', align='C', border = 1)
                                                   
    
    #getting the data from the dataframe
    pdf.ln(th+1)
    pdf.set_font('Arial', '', 8)
    for i in range(len(table['City'])):     
        name = table['Name'].iloc[i]
        city = table['City'].iloc[i]
        rating = str(table['Rating'].iloc[i])
        tag1 = table['Tag1'].iloc[i]
        tag2 = table['Tag2'].iloc[i]
        tag3 = table['Tag3'].iloc[i]
        tag4 = table['Tag4'].iloc[i]
        tag5 = table['Tag5'].iloc[i]
        phone_numbers = str(table['Phone_numbers'].iloc[i])
        range_price = str(table['Range_Price'].iloc[i])
        #filling the table
        pdf.cell(col_width, th+1, '%s' % (name), align='C', border = 1)
        pdf.cell(col_width, th+1, '%s' % (city), align='C', border = 1)
        pdf.cell(col_width, th+1, '%s' % (rating), align='C', border = 1)
        pdf.cell(col_width, th+1, '%s' % (tag1), align='C', border = 1)
        pdf.cell(col_width, th+1, '%s' % (tag2), align='C', border = 1)
        pdf.cell(col_width, th+1, '%s' % (tag3), align='C', border = 1)
        pdf.cell(col_width, th+1, '%s' % (tag4), align='C', border = 1)
        pdf.cell(col_width, th+1, '%s' % (tag5), align='C', border = 1)
        pdf.cell(col_width, th+1, '%s' % (phone_numbers), align='C', border = 1)
        pdf.cell(col_width, th+1, '%s' % (range_price), align='C', border = 1)
        
        
        pdf.ln(th+1)
    #picture Bon appétit!
    pdf.image('./src/pictures.png',10,13,9,8,'PNG')

    #pdf location
    pdf.output('./output/Best_restaurants')# pdf saved in output folder