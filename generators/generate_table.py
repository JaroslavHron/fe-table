import os
import jinja2

loader = jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), "templates"))
templates = jinja2.Environment(loader=loader)

element = templates.get_template("table.html")

elements = {
    "P1_tetrahedron": {
        "label": "\mathsf{P}_\mathsf{1}",
        "dimension": 4,
        "image": "P1_tetrahedron.png",
        "weight_functions": "\dof{4}{0}{0}{0}{1} = 4",
        "exterior_calc": "\Pm{1}{0}{3}",
        "code": '("P", tetrahedron, 1)',
        "code_alt": 'FiniteElement("P-", tetrahedron, 2, 1)',
        "color": "green"

    }
}


finite_element_table = { "table" : [
    [
        [
            ["P1_interval", "dP0_interval", None, None],
            ["P2_interval", "dP1_interval", None, None],
            ["P3_interval", "dP2_interval", None, None],
        ],
        [
            ["P1_triangle", "RT1_triangle", "dP0_triangle", None],
            ["P2_triangle", "RT2_triangle", "dP1_triangle", None],
            ["P3_triangle", "RT3_triangle", "dP2_triangle", None]
        ],
        [
            ["P1_tetrahedron", "N11e_tetrahedron", "N11f_tetrahedron", "dP0_tetrahedron"],
            ["P2_tetrahedron", "N12e_tetrahedron", "N12f_tetrahedron", "dP1_tetrahedron"],
            ["P3_tetrahedron", "N13e_tetrahedron", "N13f_tetrahedron", "dP2_tetrahedron"]
        ],
    ],
    [
        [
            ["P1_interval", "dP0_interval", None, None],
            ["P2_interval", "dP1_interval", None, None],
            ["P3_interval", "dP2_interval", None, None],
        ],
        [
            ["P1_triangle", "RT1_triangle", "dP0_triangle", None],
            ["P2_triangle", "RT2_triangle", "dP1_triangle", None],
            ["P3_triangle", "RT3_triangle", "dP2_triangle", None]
        ],
        [
            ["P1_tetrahedron", "N11e_tetrahedron", "N11f_tetrahedron", "dP0_tetrahedron"],
            ["P2_tetrahedron", "N12e_tetrahedron", "N12f_tetrahedron", "dP1_tetrahedron"],
            ["P3_tetrahedron", "N13e_tetrahedron", "N13f_tetrahedron", "dP2_tetrahedron"]
        ],
    ],
]}

generated = element.render(finite_element_table)

print generated




    # {
    #     "id": "P2_tetrahedron",
    #     "color": "green",
    #     "dimension": 10,
    #     "symbol": "\mathrm{P}_2",
    #     "html_symbol": "P<sub>2</sub>",
    #     "weight_functions": "\dof{4}{1}{0}{0}{1} \pl \dof{6}{0}{1}{1}{1} = 10",
    #     "exterior_calc": "\Pm{2}{0}{3}",
    #     "code": '("P", tetrahedron, 2)'
    # },
    # {
    #     "id": "P3_tetrahedron",
    #     "color": "green",
    #     "dimension": 20,
    #     "symbol": "\mathrm{P}_3",
    #     "html_symbol": "P<sub>3</sub>",
    #     "weight_functions": "\dof{4}{2}{0}{0}{1} \pl \dof{6}{1}{1}{1}{2} \pl \dof{4}{0}{2}{2}{1} = 20",
    #     "exterior_calc": "\Pm{3}{0}{3}",
    #     "code": '("P", tetrahedron, 3)'
    # },
    # {
    #     "id": "",
    #     "color": "",
    #     "dimension": ,
    #     "symbol": "",
    #     "html_symbol": "",
    #     "weight_functions": "",
    #     "exterior_calc": "",
    #     "code": ''
    # },
#}
